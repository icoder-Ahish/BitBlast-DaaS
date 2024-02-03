# api/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Project, Cluster, Db_credentials, Db_credentials
from .serializers import projectSerializers, ClusterSerializers
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
import requests
import zipfile
import io
from django.http import JsonResponse
import time
# from rest_framework.decorators import action


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = projectSerializers

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        project_name = request.data.get('project_name')
        print (user_id)
        if not user_id:
            return Response({
                "error":"user_id is required "

            },status = status.HTTP_400_BAD_REQUEST)
        if not project_name:            
            return Response({
                "error":"project name is required "

            },status = status.HTTP_400_BAD_REQUEST)   

        existing_project = Project.objects.filter(project_name= project_name).exists()
        print (existing_project)

        if existing_project == True:
            return Response({
                "error":"project Already exists"
            },status = status.HTTP_400_BAD_REQUEST) 
        try:
            user = User.objects.get(pk= user_id)
            print (user)
        except User.DoestNotExist:
            return Response({"error": "User with the provided ID does not exist."},
                            status=status.HTTP_404_NOT_FOUND)  

        project= Project(user= user, project_name = project_name) 
        project.save()
        serializer= projectSerializers(project)

        return Response(
            serializer.data,status = status.HTTP_201_CREATED)   

    
    @action(detail=True, methods=['PUT'])
    def rename_project(self, request, pk=None): 
        """
        Rename a project by its ID.

        Expected JSON payload:
        {
            "new_project_name": "new_name"
        }
        """
        project = self.get_object()
        new_project_name = request.data.get('new_project_name')

        if not new_project_name:
            return Response({
                "error": "new_project_name is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        existing_project = Project.objects.exclude(pk=project.id).filter(project_name=new_project_name).exists()

        if existing_project:
            return Response({
                "error": "Project with the new name already exists"
            }, status=status.HTTP_400_BAD_REQUEST)

        project.project_name = new_project_name
        project.save()

        serializer = projectSerializers(project)
        return Response(serializer.data, status=status.HTTP_200_OK)         

@api_view(['GET'])
def get_projects_by_user(request, user_id):
    projects = Project.objects.filter(user_id=user_id)
    serializer = projectSerializers(projects, many=True)
    return Response(serializer.data)
 
   
# CLUSTER CREATE API GET CLUSTER BY USER ID AND & PROJECT I

temp_variables = {}
clusterName = ''
clusterType = ''
databaseVersion = ''
providerName = ''
userId = ''
projectID = ''

	
class ClusterViewSet(viewsets.ModelViewSet):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializers

    def create(self, request, *args, **kwargs):
        global temp_variables 
        global clusterName 
        global clusterType 
        global databaseVersion 
        global providerName 
        global userId 
        global projectId 

        username = request.data.get('db_user')
        password = request.data.get('db_password')
        user_id = request.data.get('user')
        project_id = request.data.get('project')
        cluster_name = request.data.get('cluster_name')
        cluster_type = request.data.get('cluster_type')
        database_version = request.data.get('postgres_version')
        provider_name = request.data.get('provider')
        provider_endpoint = request.data.get('provider_endpoint')
        provider_access_token = request.data.get('provider_access_token')
        provider_secret_key = request.data.get('provider_secret_key')

        # Adding global variable
        clusterName = cluster_name
        clusterType = cluster_type
        databaseVersion = database_version
        providerName = provider_name
        userId = user_id
        projectId = project_id

        temp_variables = {
            'username': username,
            'password': password,
            'cluster_name': cluster_name,   
            'postgres_version': database_version,
        }
        print(f'Create function global variavle {clusterType} and {userId}')

        # Check if cluster with the same name already exists in the project
        existing_cluster = Cluster.objects.filter(project=project_id, cluster_name=cluster_name).exists()

        if existing_cluster:
            return Response({"error": "Cluster with the same name already exists in the project"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=user_id)
            project = Project.objects.get(pk=project_id)
        except User.DoesNotExist:
            return Response({"error": "User with the provided ID does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Project.DoesNotExist:
            return Response({"error": "No Project! has been selected.."}, status=status.HTTP_404_NOT_FOUND)
   
        project_id = "1"
        private_token = "glpat-QnYftX2oXsc9N5xSxG4n"
        base_url = "http://gitlab-ce.os3.com/api/v4/"

        # project_id = "132"
        # private_token = "GDNoxgBaU_vQ_Q6QzjyQ"
        # base_url = "https://gitlab.os3.com/api/v4/"


        headers = {"PRIVATE-TOKEN": private_token}
        cluster_type1 = False
     


        if provider_name == 'Kubernetes' and cluster_type == 'Standalone':
            print ("k8s pipeline")
            response = trigger_single(base_url, project_id, headers, 'deploy-postgres-k8s')
            if response == 200:
                print("Cluster save.....")
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    provider=provider_name
                )
                cluster.save()
                serializer = ClusterSerializers(cluster)
                return Response(serializer.data, status=status.HTTP_201_CREATED)



        elif provider_name == 'Cloudstack' and cluster_type == 'Standalone':
            response = trigger_single(base_url, project_id, headers, 'infra-and-db')
            print("CloudStack branch trigger.....")
            if response == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    provider=provider_name
                )
                cluster.save()
                serializer = ClusterSerializers(cluster)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:            
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
        
    @action(detail=False, methods=['get'])
    def check_cluster_exists(self, request, *args, **kwargs):
        """
        Check if a cluster with the given name already exists in the project.
        """
        cluster_name = request.query_params.get('cluster_name', None)
        project_id = request.query_params.get('project_id', None)

        if not cluster_name or not project_id:
            return Response({"error": "Cluster name and project ID are required parameters."}, status=status.HTTP_400_BAD_REQUEST)

        existing_cluster = Cluster.objects.filter( cluster_name=cluster_name).exists()

        if existing_cluster:
            return Response({"exists": True}, status=status.HTTP_200_OK)
        else:
            return Response({"exists": False}, status=status.HTTP_200_OK)
   
    
    def get_pipeline_status(self, request):
        global clusterName
        global clusterType
        global databaseVersion
        global providerName
        global userId
        global projectID
 
        print(f'global variable get pipeline status and artifact start {clusterName}, and {clusterType}, {projectID}')
        # Replace these variables with your actual GitLab project ID and private token
        project_id = "1"
        private_token = "glpat-QnYftX2oXsc9N5xSxG4n"
        base_url = "http://gitlab-ce.os3.com/api/v4/"


        headers = {"PRIVATE-TOKEN": private_token}
        pipeline_count = 1

        # Get the statuses of the latest pipelines
        latest_pipeline_statuses = get_latest_pipeline_statuses(base_url, project_id, headers, pipeline_count)

        # Get the artifacts for each of the latest pipelines
        all_artifacts = []
        for pipeline_status in latest_pipeline_statuses:
            pipeline_id = pipeline_status["id"]
            artifacts = get_latest_pipeline_artifacts(base_url, project_id, headers, pipeline_id, clusterName,clusterType,databaseVersion,providerName,userId,projectID)
            all_artifacts.append({"status": pipeline_status["status"], "artifacts": artifacts})

        return JsonResponse({"pipelines": all_artifacts})

class ClusterDeleteViewSet(viewsets.ModelViewSet):
   
    def create(self , request, *args, **kwargs): 
        print('delete-cluster')
        global clusterName 
        clusterName  = request.data.get('cluster_name')
        

        try:
             # Check if the cluster exists in the database
            cluster = Cluster.objects.get(cluster_name=clusterName)
            

            # Delete the cluster from the databas
        
     

            project_id = "1"
            private_token = "glpat-QnYftX2oXsc9N5xSxG4n"
            base_url = "http://gitlab-ce.os3.com/api/v4/"

            headers = {"PRIVATE-TOKEN" : private_token}

            branch_name = 'destroy'  # Replace with the actual branch name for destroy pipeline

            # Trigger the "Destroy" pipeline
            response = trigger_single(base_url, project_id, headers, branch_name)

            if response == 200:
                cluster.delete()
                return Response({"message": "Destroy pipeline triggered successfully."},
                                status=status.HTTP_200_OK)
            else:
                return Response({"error": "Failed to trigger Destroy pipeline."},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Cluster.DoesNotExist:
            return Response({"error": "Cluster not found."},
                            status=status.HTTP_404_NOT_FOUND)


# def trigger_infra(base_url, project_id, headers, branch_name):
#     formData = {
#         "ref": branch_name,
#     }
#     # print(formData)
#     response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=formData, verify=False)

#     if response.status_code == 201:
#         return 200
#     else:
#         return {"error": f"Failed to trigger the pipeline. Status code: {response.status_code}"}


def trigger_single(base_url, project_id, headers, branch_name):
    formData = {
        "ref": branch_name,
    }
    # print(formData)

    response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=formData,
                             verify=False)

    if response.status_code != 201:
        return {"error": f"Failed to create cluster. Status code: {response.status_code}"}

    pipeline_id = response.json().get("id")
    pipeline_status = "pending"

    while pipeline_status in ["pending", "running"]:
        time.sleep(1)

        pipeline_info_response = requests.get(base_url + f"projects/{project_id}/pipelines/{pipeline_id}",
                                              headers=headers, verify=False)
        pipeline_info = pipeline_info_response.json()
        pipeline_status = pipeline_info.get("status")

    if pipeline_status == "success":
        return 200
    else:
        return {"error": f"Pipeline failed with status: {pipeline_status}"}
   


# Status fetch function
def get_latest_pipeline_statuses(base_url, project_id, headers, count=1):
    response = requests.get(base_url + f"projects/{project_id}/pipelines", headers=headers, verify=False)

    if response.status_code != 200:
        raise ValueError(f"Error fetching pipelines: {response.status_code}, {response.json()}")

    pipelines = response.json()
    if not pipelines:
        return []

    latest_pipelines = pipelines[:count]
    latest_statuses = []

    for pipeline in latest_pipelines:
        latest_status = pipeline['status']
        latest_statuses.append({"id": pipeline['id'], "status": latest_status})

    return latest_statuses



def get_latest_pipeline_artifacts(base_url, project_id, headers, pipeline_id, clusterName,clusterType,databaseVersion,providerName,userId,projectID):
    user = User.objects.get(pk=userId)
    project = Project.objects.get(pk=projectId)
    response = requests.get(base_url + f"projects/{project_id}/pipelines/{pipeline_id}/jobs", headers=headers, verify=False)
    print(f'cluster name artifatcat wale function se {clusterName} and userId {userId} and {clusterType}')
    if response.status_code != 200:
        raise ValueError(f"Error fetching pipeline jobs: {response.status_code}, {response.json()}")

    jobs = response.json()
    artifacts = []
    # customer_name = request.POST.get('customer_name', '')
    for job in jobs:
        response = requests.get(base_url + f"projects/{project_id}/jobs/{job['id']}/artifacts", headers=headers, verify=False)
        if response.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_file:
                # Modify the following to fetch the required artifacts
                required_artifacts = ['info.txt']
                for artifact_name in required_artifacts:
                    if artifact_name in zip_file.namelist():
                        content = zip_file.read(artifact_name).decode('utf-8')
                        artifacts.append({"filename": artifact_name, "content": content})
                        
                        # Create a new PipelineArtifact instance and save it to the database
                        # Check if an artifact with the same filename and pipeline ID already exists
                        existing_artifact = Db_credentials.objects.filter(
                            pipeline_id=pipeline_id,
                            filename=artifact_name
                        ).first()

                        if existing_artifact:
                            # Update the content of the existing artifact
                            existing_artifact.content = content
                            existing_artifact.save()
                        else:
                            print('artifacts save')
                            # Create a new Db_credentials instance and save it to the database
                            artifact = Db_credentials(
                                user = user,
                                project = project,
                                cluster_name = clusterName,
                                cluster_type = clusterType,
                                database_version= databaseVersion,
                                provider_name= providerName,
                                pipeline_id=pipeline_id,
                                filename=artifact_name,
                                content=content,
                            )
                            artifact.save()

    return artifacts


def display_artifacts(request):
    # Retrieve all saved artifacts from the database
    artifacts = Db_credentials.objects.all()

    # Prepare a list to hold artifact data
    artifacts_data = []

    for artifact in artifacts:
        artifact_data = {
            'clusterName' : artifact.clusterName,
            'pipeline_id': artifact.pipeline_id,
            'filename': artifact.filename,
            'content': artifact.content,
            
        }
        artifacts_data.append(artifact_data)

  
    return JsonResponse({'artifacts': artifacts_data})



def get_variables(request):
    global temp_variables

    # Your code here, using the retrieved values
    username = temp_variables.get('username', '')
    password = temp_variables.get('password', '')
    cluster_name = temp_variables.get('cluster_name', '')
    postgres_version = temp_variables.get('postgres_version', '')
    deleteCluster_name = clusterName
    print(deleteCluster_name)

    data = {
        'username': username,
        'password': password,
        'database_name': cluster_name,
        'postgres_version': postgres_version,
        'delete-cluster' : deleteCluster_name,
    }

    return JsonResponse(data)

def extract_host(content):
    import re
    match = re.search(r'HOST:\s*([\d\.]+)', content)
    if match:
        return match.group(1)
    return None

def display_clusters(request):
    artifacts = Db_credentials.objects.all()

    # Prepare a list to hold artifact data
    artifacts_data = []

    for artifact in artifacts:
        host_ip = extract_host(artifact.content)

    clusters = Cluster.objects.all()

    # Prepare a list to hold cluster data
    clusters_data = []

    for cluster in clusters:
        cluster_data = {
            'targets': [f"{host_ip}:9187"],
            'labels':{
            'instance': cluster.cluster_name,
            'cluster_type': cluster.cluster_type,
            'database_version': cluster.database_version,
            'provider': cluster.provider,
            }}
        clusters_data.append(cluster_data)

    result_data = clusters_data

    # Return the combined data as JSON response
    return JsonResponse(result_data,safe=False)


from .serializers import ClusterSerializers
@api_view(['GET'])
def get_clusters_details(request):
    clusters = Cluster.objects.filter(user_id=user_id)
    serializer = ClusterSerializers(clusters, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_clusters_by_user(request, user_id):
    clusters = Cluster.objects.filter(user_id=user_id)
    serializer = ClusterSerializers(clusters, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_clusters_by_project(request, project_id):
    clusters = Cluster.objects.filter(project_id=project_id)
    serializer = ClusterSerializers(clusters, many=True)
    return Response(serializer.data)


from rest_framework import generics
from rest_framework.response import Response
from .models import Db_credentials
from .serializers import DbcredentialsSerializer

class ContentByClusterNameView(generics.ListAPIView):
    serializer_class = DbcredentialsSerializer

    def get_queryset(self):
        cluster_name = self.kwargs['cluster_name']
        return Db_credentials.objects.filter(clusterName=cluster_name)
# Use the official Jupyter Data Science Notebook as a base image
FROM jupyter/datascience-notebook

# Set the working directory in the container
WORKDIR /usr/src/app

# Install MLflow
RUN pip install mlflow boto3 psycopg2-binary awscli

# Copy the local files into the container
COPY . .

# Expose ports for Jupyter Lab and MLflow UI
EXPOSE 8888 5001

# Set the default command to run MLflow and start Jupyter Lab
CMD bash -c "\
    mlflow server \
    --backend-store-uri ${MLFLOW_TRACKING_URI} \
    --default-artifact-root ${MLFLOW_DEFAULT_ARTIFACT_ROOT} \
    --host 0.0.0.0 --port 5001 & \
    start-notebook.sh --NotebookApp.token='' --NotebookApp.password='' \
    "
# Define a base image
FROM continuumio/miniconda3

# Create (mkdir) /ex01 and cd /ex01 on your image
WORKDIR /ex01

# Copy everything from current directory to working directory
COPY * .

# Create a conda virtual environment
RUN conda env create -n ex01 -f environment.yml

# Install fastAPI clip in the environment
RUN conda install -n ex01 fastapi[standard]

# Expose port 8000 for fastapi
EXPOSE 8000

<<<<<<< HEAD
# run the ex01.py as fastapi server.
CMD ["conda", "run", "--no-capture-output", "-n", "ex01", "fastapi", "dev", "ex01.py", "--port=8000", "--host=0.0.0.0"]

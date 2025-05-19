# ImageProcessing

## How to use

- Make sure you have [Docker](https://docs.docker.com/get-docker/) installed on your system.

## How to build and run the app

1. **Clone this repository and enter the project folder:**

   ```sh
   git clone <repo-url>
   cd Test_Backend_INbest
   ```

2. **Build the Docker image:**

   ```sh
   docker build -t imageprocessing-app .
   ```

3. **Run the container:**

   ```sh
   docker run -p 5000:5000 imageprocessing-app
   ```

4. **Open your browser and go to:**

   ```
   http://localhost:5000
   ```
# ImageProcessing

## How to use

- Make sure you have [Docker](https://docs.docker.com/get-docker/) installed on your system.

## How to build and run the app with Docker

1. **Clone this repository and enter the project folder:**

   ```sh
   git clone <repo-url>
   cd Test_Backend_INbest
   ```

2. **Build the Docker image:**

   ```sh
   docker build -t imageprocessing-app .
   ```

3. **Run the container:**

   ```sh
   docker run -p 5000:5000 imageprocessing-app
   ```

4. **Open your browser and go to:**

   ```
   http://localhost:5000
   ```

## How to run the app using Python virtual environment (venv)

1. **Clone this repository and enter the project folder:**

   ```sh
   git clone <repo-url>
   cd Test_Backend_INbest
   ```

2. **Create and activate a virtual environment:**

   On Linux:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```sh
   python app.py
   ```

5. **Open your browser and go to:**

   ```
   http://localhost:5000
   ```


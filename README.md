# ImageProcessing

## How to run

- Make sure you have [Docker](https://docs.docker.com/get-docker/) installed on your system.

## How to build and run the app with Docker

1. **Clone this repository and enter the project folder:**

   ```sh
   git clone <repo-url>
   cd ImageProcessing
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
   cd ImageProcessing
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

## How to use the app

1. **Register or log in:**  
   On the home page, click **"Create User"** to register a new account or **"Login"** if you already have one.

2. **Upload an image:**  
   After logging in, go to the image upload section. Click **"Browse"** to select an image from your computer and then click **"Upload"**.  
   You will see a preview of the image before uploading.

3. **Process the image:**  
   After uploading, you will be taken to the processing menu. Here you can:
   - Rotate the image by clicking **"Rotate Image"**.
   - Convert the image to grayscale by clicking **"Gray Scale"**.
   - Save the processed image by clicking **"Save Processed Image"**.

4. **View or download saved images:**  
   Click **"View Saved Images"** to see all images you have saved.  
   You can preview or download any image from this list.

5. **Upload another image:**  
   Use the **"Back"** button in the processing menu to return to the upload page and process another image.
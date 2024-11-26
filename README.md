
Instructions to Use the Template

1. **Prepare the JSON Files**:

   - Save the `project_structure.json` and `file_contents.json` files in the same directory as `generate_project.py`.
   - In `file_contents.json`, include the actual code content for each file, using placeholders where personal information is needed.

2. **Run the Script**:

   Execute the script using the command:

   ```bash
   python3 generate_project.py
   ```

   **Provide Personal Information**:

   When prompted, enter your name, email, and GitHub username.

3. **Activate Virtual Environment**:

   Change directory into `face_motion_tracker` and activate the virtual environment:

   ```bash
   cd face_motion_tracker
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Run the Application**:

   To run the application, execute:

   ```bash
   face-motion-tracker
   ```

   Or run directly:

   ```bash
   python src/main.py
   ```

5. **Refer to readme.txt**:

   Follow the instructions in `readme.txt` for more details on running and testing the application.
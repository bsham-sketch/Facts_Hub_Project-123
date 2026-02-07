# Facts Hub - Application Startup Guide
# Facts Hub - Application Startup Guide
# Facts Hub - Application Startup Guide

## Quick Start Instructions

### 1. Backend Setup (Django)
Open a new terminal/command prompt and run:

```bash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt
python manage.py runserver
```

The backend will be available at `http://localhost:8000`

### 2. Frontend Setup (React)
Open a **new** terminal/command prompt and run:

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:3000`

## PowerShell Execution Policy Fix

If you get the "running scripts is disabled" error in PowerShell, run this command first:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Or use Command Prompt (cmd.exe) instead of PowerShell:

```cmd
cd frontend
npm install
npm run dev
```

## Alternative: Use Command Prompt

If PowerShell continues to have issues, use Command Prompt (cmd.exe):

1. Press `Win + R`, type `cmd`, press Enter
2. Navigate to your project directory
3. Run the commands from there

## Application URLs

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000/api/
- **Django Admin**: http://localhost:8000/admin/

## Testing the API

Once both servers are running, test the API endpoints:

```bash
# Test categories endpoint
curl http://localhost:8000/api/categories/

# Test facts endpoint
curl http://localhost:8000/api/facts/
```

## Troubleshooting

### Common Issues:

1. **Port already in use**: Try `python manage.py runserver 8001` for backend
2. **npm install fails**: Delete `node_modules` and `package-lock.json`, then run `npm install` again
3. **CORS errors**: Ensure backend is running and CORS is enabled in settings
4. **PowerShell execution policy**: Use Command Prompt or fix execution policy as shown above

### Verify Installation:

1. Backend running: Visit http://localhost:8000 - should see Django welcome page
2. Frontend running: Visit http://localhost:3000 - should see Facts Hub application
3. API working: Visit http://localhost:8000/api/categories/ - should see JSON response

## Project Structure

```
Facts-projects/
├── backend/          # Django REST API
│   ├── manage.py
│   ├── requirements.txt
│   └── facts_api/
└── frontend/         # React Application
    ├── package.json
    ├── src/
    └── public/
```

## Next Steps

1. Start both servers
2. Open http://localhost:3000 in your browser
3. Explore the application:
   - Browse categories
   - View facts
   - Add new facts
   - Delete facts
4. The application supports full CRUD operations with a responsive, modern UI
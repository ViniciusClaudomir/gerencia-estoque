import uvicorn
from dotenv import load_dotenv

load_dotenv('.env') 


if __name__ == "__main__":
    uvicorn.run("app.api.main:app",
                host="0.0.0.0",
                port=8000,
                reload=True,       
                log_level="info"   
    )
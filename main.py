from fastapi import FastAPI

# Create A FastAPI instance


app = FastAPI()


# Health check endpoint

@app.get("/health")
async def health_check():
    return {"status": "healthy"}




@app.get("/")
async def root():
    return {"message":"Hello world"}


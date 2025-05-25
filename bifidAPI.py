from typing import List, Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from bifid import bifid_encrypt, bifid_decrypt, shuffle_table, classical_table

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BifidCoderType(str):
    ENCRYPTION = "encryption"
    DECRYPTION = "decryption"

class BifidCipher(BaseModel):
    text: str
    table: Union[str, List[List[str]]] 
    coder_type: str  

class BifidCipherResult(BaseModel):
    result: str

def process_bifid_cipher(data: BifidCipher) -> str:
    if isinstance(data.table, str):
        if data.table == "classical_table":
            table = classical_table
        elif data.table == "shuffled_table":
            table = shuffle_table(classical_table)
        else:
            raise HTTPException(status_code=400, detail="Invalid table name")
    elif isinstance(data.table, list):
        table = data.table
    else:
        raise HTTPException(status_code=400, detail="Invalid table format")

    if data.coder_type == BifidCoderType.ENCRYPTION:
        return bifid_encrypt(data.text, table)
    elif data.coder_type == BifidCoderType.DECRYPTION:
        return bifid_decrypt(data.text, table)
    else:
        raise HTTPException(status_code=400, detail="Invalid coder_type")

@app.post("/api/bifid", response_model=BifidCipherResult)
def bifid_enc(data: BifidCipher):
    result = process_bifid_cipher(data)
    return {"result": result}

@app.get("/api/bifid/table")
def bifid_shuffle_table():
    return {"table": shuffle_table(classical_table)}

from fastapi import APIRouter, Response, Request, UploadFile, File
from web.service.qalib import QaLibService
from typing import List

qalib_api = APIRouter()


@qalib_api.post("/v1/getInfo")
async def qalib_info(request: Request, response: Response):
    return await QaLibService(request, response).info()


@qalib_api.post("/v1/addDocs")
async def qalib_add_docs(request: Request, response: Response, files: List[UploadFile] = File(...)):
    return await QaLibService(request, response).add_docs(files)


@qalib_api.post("/v1/getSampleInfo")
async def qalib_get_sample_info(request: Request, response: Response):
    return await QaLibService(request, response).get_sample_info()

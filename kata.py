import aiohttp
import asyncio
import ssl
import json
from aiohttp import FormData


class App:
    NAME = 'Kata'
    is_token_expiring = False
    base_url='https://10.10.101.200:443/kata/scanner/v1/sensors/2cc5c618-8051-11ed-a1eb-0242ac120002'
    sslcontext= ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        #need get cert function in base app class
    sslcontext.load_cert_chain(
            'client.crt',
            'C:/Users/Jiraya/Desktop/client.key'
            )
    
    async def ksc_scan(self,payload):
        url=f'{self.base_url}/scans'    
        params = {
        'sensorInstanceId': 'instance1',
        }
        
        data = FormData()
        data.add_field('content', open(payload['path'], 'rb'))
        
        data.add_field('content', payload['content'])
        data.add_field('scanId', payload['id'])
        data.add_field('objectType', 'file')
        
        sslcontext=self.sslcontext  #iki tane tANIMLAMA
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=url,
                params=params,
                data=data,
                ssl=sslcontext,
            ) as response:
                return await response.text()
            
    async def delete_file(self,payload):
        url=f'{self.base_url}/scans/{payload["file_no"]}'
        sslcontext=self.sslcontext
        
        async with aiohttp.ClientSession() as session:
            async with session.delete(url,
                                      ssl=sslcontext,
                                      ) as response:
                return await response.json()
            
            
    async def file_result(self):
        url=f'{self.base_url}/scans/state'
        sslcontext=self.sslcontext
        
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=url,
                ssl=sslcontext,
            ) as response:
                return await response.json()
            
    async def detectedtype(self,payload):
        url=f'{self.base_url}/detects'
        sslcontext=self.sslcontext
        
        params={
            'detect_type' : payload['type'],
            'limit' : payload['no'],
            'token' : '7b226f6666736574223a20307d',          
        }
            
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=url,
                params=params,
                ssl=sslcontext,
            ) as response : 
                return await response.json()
            
    async def object_get_restiraction(self):
        url=f'{self.base_url}/scans/filters'
        sslcontext=self.sslcontext
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=url,
                ssl=sslcontext,
            ) as response :
                return await response.json()
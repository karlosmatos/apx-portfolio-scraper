import scrapy
import requests
import json
import os
import pandas as pd

from companies_script import extract_field


class ApxSpiderSpider(scrapy.Spider):
    name = 'apx_spider'
    allowed_domains = ['apx.vc']
    start_urls = ['https://apx.vc/our-portfolio']

    custom_settings = {
        'LOG_LEVEL': 'ERROR',
        'USER_AGENT': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        'DEFAULT_REQUEST_HEADERS': {
            'Referer': 'https://www.google.com'
        }
    }

    def __init__(self):
        self.parse()

    def __del__(self):
        pass

    def parse(self):
        headers = {
            'authority': 'apx.network',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en,cs;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://apx.network',
            'referer': 'https://apx.network/',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'x-bubble-breaking-revision': '5',
            'x-bubble-epoch-id': '1701798422990x848212993326742400',
            'x-bubble-epoch-name': 'Epoch: Runmode page fully loaded',
            'x-bubble-fiber-id': '1701798423880x274548207296984030',
            'x-bubble-pl': '1701798421724x2306',
            'x-bubble-r': 'https://apx.network/portfolio?portfolio=APX',
            'x-requested-with': 'XMLHttpRequest',
        }

        json_data = {
            'z': 'boDR7TVSoooqq77Y2iZFFM7iZo1ZquYFREB1Se0YOc4zThQ3ZRLgucd/nP/OtHFiCbUF9QsP2kT9iuUuW4v1Ltk2dzICXzQkxNxlA+Uh6AewaTgd54PSlny+WDjXjwYb859hYGCW6LQW0770OXacQNIICjh2IgqzNzv3hFIN+gpZ+MHPczGN4qIuDibXn37cWWfeeOUdM3WD5M2OeG810gugEAKWdkMBhdHdN3Nz6asgnJZz9Wu97VL2uRecM4pMUoGwzmUM2qmA+2FQLg+0CXdVFjbDiR9B06hOvfxff0pVFPxxJEQO4zDf8b4zl50cWB6lUHsaXYIRWQON8GCe8wwMRR7z0e0hETc/NaOgGP97aEhi8y2OLlFVSBqPh9/yPvJ7WZ/Ectfu31ljT5E13ATLPINn0nMcL2vLOOWC8oBhl5ekCmPJdAj+2qZt0Fy8lS1+F+EXxuoh3aOPxxJWAzqN4GG/VZzkMoFdDLLaC3p20fSJRgPwvyFSFgsY8dZBitLd0TNOFQp/8Ff6xIpt7kszzlMcLVeeaYy1b6bylOgeqmr30HSouxK/7N2zKl/0cEP8PV4VP5QajRwLUeIzm2ZSsAvs6bLKKxalkk4u3EPXb1IE1MUGH5YiMnuOtLls',
            'y': 'EdloEaLT99C6aMhfZMC4aA==',
            'x': 'qKFaTysLa8bPq7iv6gLaUQX6C8fQ5Hke/8DJViwmcG0=',
        }

        response = requests.post('https://apx.network/elasticsearch/search', headers=headers, json=json_data)
        with open('companies.json', 'w') as f:
            json.dump(response.json(), f)

        headers['x-bubble-epoch-id'] = '1701800015185x407901532622083840'
        headers['x-bubble-fiber-id'] = '1701800016778x330978079358221300'
        headers['x-bubble-pl'] = '1701800013892x1444'

        json_data = {
            'z': 'GUweKWRA1jJj8VPGpQFmMOrdzVMRYIt2rLX97TY8E0+Z2PE5rqJvkTt9lbnRStUBUNir3yRfbJ8yq362yThgOY5w6PgOTdKNOMW8g1rVfmisWuSgVngjz/F+EKowGtKQMa7Ujfrp/xJKpIC9UPNmkpg4V5buMhmw1lPIuioMb3ZPJm0R702K5WeQdAZ4y4qS8g1iH32NpZTxi0GQ9GFIXDTLp1aJ1DR02Vm4ddgv5pXqzrHHcaO/Zk9Jy59K776plUojYhtJXAZeRbERfNbuf9wbgY07I7CZDS3vLit2dyx7KLIZV0iBULAea+6ENoIlKBuNuhXBqc5txo/o44FaYilk/McKVifwZsPymlfxJO3DRw8i30sJon7uI7VB4JPP/4C/ONNyq7/hntUv10LlaHALeaCd5DnMGZEmOllqD2upRUsL+lMuo1emTkLYYd9cWLw4HXaAtKUBQXXIBg4pFrEEZax8M/nJP+s5v7HrIBBiQM3W8R36+oy4AkHHCkbAQBW6ufhUilwUmQYtsL6ArqKtQ5wMWUDHY/SGk4tiCVnYtZYtFT5KTw8GfJmSP6yONzaub0is5cFvIxvXU2SiwaB3En6mcRdeeGe+AYmnTfjO9XuUEDH4XmZxIeAcaKRfajsJxVksbVj94YXfS8UmPC/RqP+UgoDGgZTTqVhPuwWSkYZtsdNMYlqNFpsVGnFBenQwaV5TqpoaSMiYaty0j4chgLbk4A0doUuvnZ5mK7nkTiihO3Eg0p1UG5DoLeK9QZJVwu8wyRNQ3a3rS9gjZLQ42zbsK10bAvu+mlidyHFUpG8jl0iHqDlX2QgmVYlueL3q7B6R+sZDantxHOAEe6zHLLn8TIVo8IGLHkqx6ukqGGLo/V15OY+GYNFUY1xT9jHOOI/Bct3CLBoFB9EvVj0J2WXJHxSltRc7SiT2PmtsY8QrSC+9jt/grTL3TkhEEd4srVdBJOV4kR2tNojii7oXkHYCr7QIzrFm1tUTKL0As0FMHJGUfbmUBXg/63d5KQXIAYmK9xE45YHp37NU41l0GOKAfH86ran1BGg/kU+z5s1w6a7xNzxiFAwdf2JE4vlq7QnnUlAdAyesyaP1MP6ujiY6qcZCuaWlZe7xFaAX5m7Wvh+P4xKo8b5YhRHI499Pm4TAhr+IQUMOWUNHQwJDHaOwfJxhjrb6Pyrev0RA/QwnJLKy9KXuoAbHNEitmKErADGlL59z5fpxNZdyK0GVHkyos/GEBsXA/VVOaQzK0eTOiPUaWOAomBYz36ru5O9ld4GOb2fyvnwlIhltWmCvBgFPjLCMzu4F0+y4huP9GMPiu2IHiKjEOQb7M2kHuOyNoMntzVwoJAyldP62Wngdjd++ifz+fGDqapiYfHRhLLidh78hHPlhC4rz+i2lUdtFcW1D+3dZaYu/eC8uhkK5smRVzposDT+FlB+j+lhkmmdbRQ0rXHqqyaOfQ9ALmCLo9MUfsC19JYeZq7v6nqHd5qNN2cenYDl9NlplE6TI91LkfF9bRSIz5hy1D1iQh3tbpoZahIzDM/6cSXPC64Q8bqMSeoErrREcypWImqSc7MW+0rhkBnOP8haL05+PpsABHe89MHwvIe2W0t9kr08wx8NAttRa8Kj1mt5VwIWsYpPQrSs2MRzqc29Li5tdiKBhvvw/fKAOXbmrtht+cHxHfljp1LBlMfcgVBIj4ASENs/0n61kWghc42UCVhS+RdI52JLv5dRTmQCd6zazkaNSkoaf303WaPlRKDuDXCmVH/PDgrCtimUJnF8ED4jMdoa83CqeFw4G+S4oRtMU8A==',
            'y': '/1fyIc+QGjiWCZRrrEnE6w==',
            'x': '+aqyAAVNA9jUYJxsJT5D9s9+X9LtBD7VE1JuNXzjXTE=',
        }

        response = requests.post('https://apx.network/elasticsearch/mget', headers=headers, json=json_data)
        with open('industries.json', 'w') as f:
            json.dump(response.json(), f)

        headers['x-bubble-fiber-id'] = '1701800018284x986197179391080700'

        json_data = {
            'z': '8+erInX+LR6FB9ctzmhThs0jYv73McNgL1px7ci60IFhyHUeQieaQXDJnFwPz0cMAEXOwvvzlApiuxqGMZ3VP2+bgctT3pN3bZLcHxkTdG064Xvxbb8lORiLn5tVK9zjNswI584Xlp4uvEAUx1/+muvfZ7LiT9Cj1jdRYX08X2cCQE0YGZf7746JOwILarEa5khl8fBJuxqXJ0QQ471i4iQScIj9B7J/fV72qw3EOg62s5H2Ldq3p548Y1BbVs2D+lqLZHwCR2k4EHRS6mhwE9uLt7Gka8Ywd+XVcfj6ajLukcNkcRlnQz9PKrB0IARl4GFZMfu0nkMq/Za7LRI6wsnmJVrHKweBWkRymQBO5ITPIjeqD8k4aAngNL2vktONXzIogxKgZTca22d07RqfAFSY6raoTmnv4LZp2MTb9882sXPs1owzwEPiXzyhVX7S2f4fbxjQztbIL32fQc3Vh0RMB6yA77LnwDzn1ChaGO/ZvU9KJt1l5o4ZWH/Dp5BjXDvx76BpOUOSrdtOmOAoA+jkAeRj8CVqKWlfXdiii2xFixiuWTulfcPKf5B2U9ryZBtOhoIsR8L23iRk8Pt1u/WnhqdRg3pVjapCSesqsT94vuh+reCbHEco3kGWH+wp8BqqeqLcR97RgdrjFjpiUWw0lYDOcWklNcOpiomdXALmB5haJ7ycRhjFmr5tjvRsUypnnw3bUuchPuz7x/Av5+7j+T0ZFC1jtgN7c0dmtrday5EC81V0ZEf71mIot1Mm6+EgVI4ovjcYvVnvZVfQGQGt169eUQnf6AmKKBLVfH8T1nGG3dfUbfVEQanbGGL5D45KpLDRLS6Q+4z1yphhw21QO9AiZKiSIdvKO5/O5C8UW2KmuK078oO4L50XVgDBbwGv1AAKl/9BZu/OBQWv5DyDlnBZk/IWwgzRgYaRfJtfWePQcySwhk0F6pbGU5yI4q96xKTix44a4HsMysq2b4TYNFDLDy8gGNLR7PNqcdoTB9JH8xwhv33yUHnQcqnkiNZaYNAepMrM7DKRpIiZEH6GxdAgXzozOMxidTWsf9GbaLzIu+OZqImvQq0+oXUeH3G2EWGnnqFx+GbTAFWIK6V3MWSISv6UlZ7SK1OlhyN7bS7a8Ukkh9iwR9xx4IdPXUpFeJvgNMo4a/hWLD+D1U3d3AHgOKIjd0UTw/sQAp+wbrz47QdfnnnLHYvNGuvsLWnrg49CGrcnZwL9C8tJnu3MtK2lrkXQaBYV8K1p6fYigsqpppjbBXsi7AGWlpLOtJQeIm3TmmVZvLLtTaIr9pXMCxK6czqAe2HaczkD+Dqw8/KNCeSH8b6oKlbgX5fUd+XejRz1eIofiWxhhqR2wpZlfYDO7CR9AxcLffB+//o=',
            'y': 'AI3HsKtAMEJ6+zO0v1HWCw==',
            'x': 'rxpN1zUn3/QHAvRMteWJ1jRRWAhA80xaNINoAaZRT6k=',
        }

        response = requests.post('https://apx.network/elasticsearch/mget', headers=headers, json=json_data)
        with open('revenue_models.json', 'w') as f:
            json.dump(response.json(), f)
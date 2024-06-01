import pytest
from pages.login import Login
from playwright.sync_api import Browser


@pytest.mark.smoke
class TestAdminLogin:
    def test_admin_login(self, browser: Browser):
        context = browser.new_context()
        page = context.new_page()
        m = Login(page, is_admin=True)
        # page.on('request', lambda request: print(f'>>{request.method()}: {request.url()} \n {request.all_headers()} << \n'))
        # page.on('request', lambda request: print(f'>>{request.all_headers()} << \n'))
        m.user_login()
        # cookies = context.cookies()
        # print('Cookies after logging in:', cookies)
        # storage = context.storage_state()
        # print(storage)

test = {
    'accept': '*/*', 
    'accept-encoding': 'gzip, deflate, br, zstd', 
    'accept-language': 'en-US,en;q=0.9', 
    'connection': 'keep-alive', 'content-length': '766', 'content-type': 'application/json', 
    'cookie': 'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6InBOY2JYck9KNDhHcE1nb0hCY1JkWnc9PSIsInZhbHVlIjoidk1TSHB1SmFubEFSMHY4SGNSek12U3hVNzYyeUNzUzV6by9aSnhsOGV4MVQxTHhLTlUwNnVCKzVoU2RlOEZ4SWthd0VpNXpMSllCMUVHNGpIT0YrN2Y1TVlCSUlaU3dPcmhCTnhZL09wSHQyamJWUno1RjkxcXhBNWZhUjBuRXdqNnUyb1JmUEpIUERyNGpFOEZLTngyRXJRTmx3dldKUHRTMlA0bjg1NWx3ZWpGZyt3Qy9ZaE9QZHZSQlh4WUdEbU02OE9CdWc4QWxnRmsyTjN3dU9PK0JCMDYybmc4NVlmamk5cHJHalJNOD0iLCJtYWMiOiIxZjJlNmQyMTA0ODQzNTliNGI1YjMxMzhiYTYwMmM3ZDczMjJmZTBhNjc1YzQxZjQ4NjMxZTFiZTI1ZGNiMjVlIiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6Ii9CREJCTGVnU0ZJaUdqNFB2RU9VMmc9PSIsInZhbHVlIjoic3lBVHZXWmxDTi9FWklKcGZwbTV3ajBHSWhySi9lTWlaK3VlSmhWREFFZjQxdzk1bnd3Q29SMEgzSExCTDhITHZUUDY5NFc2SDNEV05NbkNqTSt3NVdUWjF3UGhhU3c1RDA3SC9KRjJYTWRYWHVHVlBVQmhtOUpST3lXTTZ2RTUiLCJtYWMiOiI1OGUxZjEwMGIyM2U4OGU0ZjQ2Y2E2MGM0N2I5ZThhYjAzZmFiNzdhY2JlZDA2ZTRkYzM5ZTEyNGY2YzljN2NlIiwidGFnIjoiIn0%3D; residential_energy_partners_session=eyJpdiI6IkJ5bmJEMzFLdG9MM290VlJqUTNybWc9PSIsInZhbHVlIjoiR290WUpaUnBRZDZmazlsWVNWTVpyV1BTU0lHaTBQQmY4VWEvYWlrcHlpdXJ3NldFWnZmWVBSQk1TRmdEZzMyR1BDZ1dxK1FTTVhvdHVjTkdYanlROHpuMXhWMzZYM2JsTnlRUXFJQllTTlpOK3EwZ3QzQmpGU3NwYUZhZ2liYW0iLCJtYWMiOiI3YmI4ZjNhZWNmZjMxMGI4YWQwNDc4NDFkOTA4NTAzMjJiNzI1ZDZkZjJlNThjMTAyOTM0MTM3YmNkMTYxM2JlIiwidGFnIjoiIn0%3D', 
    'host': 'sb.kslndr.tech', 'origin': 'https://sb.kslndr.tech', 'referer': 'https://sb.kslndr.tech/admin', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36', 'x-livewire': '', 'sec-ch-ua': '"Chromium";v="125", "Not.A/Brand";v="24"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'} 

test = [{
        'name': 'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d', 
        'value': 'eyJpdiI6ImY2RmN2QzlGOUI0L1I0WThjNHhJN3c9PSIsInZhbHVlIjoiOXg2aGl4VTJSZ1IvTEx1M1BLT0lSZGtEeHZKTzB1Z1JQTkMrUC91K1NUaGVtQStuellQT3pJNGdwRXVrc2I3U3poaU9iMmxRa2F1ODdkQ0x4T3daRGkyMkxUQ0JBRFp1NlU4cHdRVm9EN0RwblZLdGx4dUs1d25kSmJxMTZGOVNlRmw0RVJNZ3dVeUVMZFZwWVd3WFFFSDZsRmJFbE9nbGNDSGIzbjcrUjdFZ0lPN3ZSblNESjExZDh1d1hFNTF3c0NmR2ZwaGExbXpwS21LckFVRXE4eTRIeTgrU2I2RmJxSnY1cHd1V2tXRT0iLCJtYWMiOiJkNGFmZjg5ZWZmMjU0NDE5OWYwZjA4YTJkYmM5MmI3MWQzODE3OTNhZDM0Yjg1NzAyNWQ1Y2I3NWJlZGVkMTdjIiwidGFnIjoiIn0%3D', 
        'domain': 'sb.kslndr.tech', 'path': '/', 'expires': 1751624672.905498, 'httpOnly': True, 'secure': True, 'sameSite': 'Lax'
    }, 
    {
        'name': 'XSRF-TOKEN', 
        'value': 'eyJpdiI6IkFsZ3p5SUMzQ0hHaUo0VVVBMXRlYXc9PSIsInZhbHVlIjoiYnN4TkNzTXR0VnBTS0ROcElpdHlmYnJyM0dqUjREUjRRMC8vdTE2KzBMNExneEtQZUVrbmlLZllPRjdMd2xKT1haYld2QkhOMlhiVTIwblRRNXUxSlZ0THI1UlR1d1lpRC9jQmVXR2ZGc1JrZ29DY0FyZjNMV2gzclRvVW84SEgiLCJtYWMiOiIzNTk1MWU1ZDYwYmE3NDI0NjNjOTBlYTBiODc3MTFlNTllNzk4MDQ1Y2M3YjgyOWY2YmE4NzhiZGNiMDVmODUwIiwidGFnIjoiIn0%3D',                                                                                                                             
        'domain': 'sb.kslndr.tech', 'path': '/', 'expires': 1717071874.584612, 'httpOnly': False, 'secure': True, 'sameSite': 'Lax'
    }, 
    {
        'name': 'residential_energy_partners_session', 
        'value': 'eyJpdiI6IjBQV3E0d3dZS21LbnVXYlJ4VFJ5Qnc9PSIsInZhbHVlIjoidFNtOVlKNXgvYy9DazdrL0N5NUo1NG1PRi92bFpCVTFFVmNoZHdyNjdpVW16OVc2UC9zRHhkNVVES3VIRXE3dThzRnpneGFmUGR1MXErZ00zT3k0SWYwRWFnMk55S0ZqelBCcllsbUU2K25nQ3lKcVRUa1ZjdERzOXU5OU15WUwiLCJtYWMiOiI5ZjRlZDY2Y2IyNGNlNDdlMTJkZWZkZTIwNjZkMTgwNzBkYjE0YjgxYmY3ZTcxYjY1MmM0ZjA2YjIzNTMxMDgwIiwidGFnIjoiIn0%3D', 
        'domain': 'sb.kslndr.tech', 'path': '/', 'expires': 1717071874.584798, 'httpOnly': True, 'secure': False, 'sameSite': 'Lax'
    }
]
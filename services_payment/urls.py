"""
URL configuration for services_payment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
import requests


def hello(request):
    try:
        response = requests.get("https://daveclintonn.cc/", timeout=5)
        response.raise_for_status()
        return HttpResponse(response.text, content_type="text/html")
    except Exception as e:
        return HttpResponse(
            f"""
            <html>
            <head>
                <title>Welcome</title>
                <style>
                    body {{
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        min-height: 100vh;
                        margin: 0;
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    }}
                    .container {{
                        text-align: center;
                        background: white;
                        padding: 40px;
                        border-radius: 10px;
                        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                    }}
                    h1 {{
                        color: #333;
                        margin: 0 0 20px 0;
                    }}
                    p {{
                        color: #666;
                        margin: 10px 0;
                    }}
                    a {{
                        display: inline-block;
                        margin-top: 20px;
                        padding: 10px 20px;
                        background: #667eea;
                        color: white;
                        text-decoration: none;
                        border-radius: 5px;
                        transition: background 0.3s;
                    }}
                    a:hover {{
                        background: #764ba2;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Welcome to services-payments</h1>
                    <p>Hello, David! 👋</p>
                    <p>This is your payment services API.</p>
                    <a href="https://daveclintonn.cc/" target="_blank">Visit Your Website</a>
                </div>
            </body>
            </html>
            """,
            content_type="text/html"
        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", hello, name="hello")
]

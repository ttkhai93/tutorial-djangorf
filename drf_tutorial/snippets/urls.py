from django.urls import path, include
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from snippets import views

# from snippets.views import api_root, SnippetViewSet, UserViewSet

# Bind http methods to actions
# snippet_list = SnippetViewSet.as_view(
#     {
#         "get": "list",
#         "post": "create",
#     }
# )

# snippet_detail = SnippetViewSet.as_view(
#     {
#         "get": "retrieve",
#         "put": "update",
#         "patch": "partial_update",
#         "delete": "destroy",
#     }
# )

# snippet_highlight = SnippetViewSet.as_view(
#     {
#         "get": "highlight",
#     },
#     renderer_classes=[renderers.StaticHTMLRenderer],
# )

# user_list = UserViewSet.as_view({"get": "list"})
# user_detail = UserViewSet.as_view({"get": "retrieve"})


# urlpatterns = [
#     # path("snippets/", views.snippet_list),
#     # path("snippets/<int:pk>/", views.snippet_detail),
#     path("", api_root),
#     path("snippets/", snippet_list, name="snippet-list"),
#     path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
#     path("snippets/<int:pk>/highlight/", snippet_highlight, name="snippet-highlight"),
#     path("users/", user_list, name="user-list"),
#     path("users/<int:pk>/", user_detail, name="user-detail"),
# ]

# Trade-offs
# Pros: URLs consistency, minimizes code
# Cons: Hard to custom
# => Consider to not use ViewSets if necessary

router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]
# urlpatterns = format_suffix_patterns(urlpatterns)

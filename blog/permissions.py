from rest_framework import permissions  # 限权


class IsOwnerOrReadOnIy(permissions.BasePermission):
    """自定义限权只允许对象的所有者编辑它"""
    def has_object_permission(self, request, view, obj):
        # 读取限权允许任何请求
        # 所以我们总是允许 GET HEAD OPTIONS 请求
        if request.method in permissions.SAFE_METHODS:
            return True

        # 只有该snippet的所有者才允许写限权

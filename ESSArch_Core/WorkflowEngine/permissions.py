from rest_framework import permissions


class CanRun(permissions.IsAuthenticated):
    message = "You are not allowed to run tasks"

    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('WorkflowEngine.can_run')


class CanUndo(permissions.IsAuthenticated):
    message = "You are not allowed to undo tasks"

    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('WorkflowEngine.can_undo')


class CanRetry(permissions.IsAuthenticated):
    message = "You are not allowed to retry tasks"

    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('WorkflowEngine.can_retry')

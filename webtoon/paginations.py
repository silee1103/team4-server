from rest_framework.pagination import CursorPagination


class CommentCursorPagination(CursorPagination):
    ordering = '-dtCreated'
    page_size = 30


class PaginationHandlerMixin(object):
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):

        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                                                self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class WebtoonCursorPagination(CursorPagination):
    page_size = 30
    ordering = ['-latestEpisodeCreated']


class EpisodeCursorPagination(CursorPagination):
    page_size = 30
    ordering = ['-episodeNumber']

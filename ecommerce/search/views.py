from django.http import HttpResponse
from ecommerce.api.serializer import ProductInventorySearchSerializer
from ecommerce.search.documents import ProductInventoryDocument
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView


class SearchProductInventory(APIView, LimitOffsetPagination):
    productinvetory_serializer = ProductInventorySearchSerializer
    search_document = ProductInventoryDocument

    def get(self, request, query):
        try:
            q = Q(
                "multi_match",
                query=query,
                fields=["product.name"],
                fuzziness="auto",
            ) & Q(
                "bool",
                should=[
                    Q("match", is_default=True),
                ],
                minimum_should_match=1,
            )

            search = self.search_document.search().query(q)
            response = search.execute()
            print(response)
            results = self.paginate_queryset(response, request, view=self)
            print(results)
            serializer = self.productinvetory_serializer(results, many=True)
            print(serializer.data)
            return self.get_paginated_response(serializer.data)

        except Exception as e:
            return HttpResponse(e, status=500)

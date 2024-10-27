from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *


class WarehouseAPI(APIView):
    def get(self, request):
        # Ishlab chiqarish uchun zarur bo'lgan mahsulotlar va ularning sonini belgilaymiz
        production_plan = [
            {"product_name": "Ko'ylak", "product_qty": 30},
            {"product_name": "Shim", "product_qty": 20}
        ]

        result = []
        used_materials = {}  # Avval ishlatilgan miqdorni saqlash uchun

        for plan in production_plan:
            product_name = plan["product_name"]
            product_qty = plan["product_qty"]

            # Mahsulot uchun kerakli xomashyolarni olamiz
            product_materials = ProductMaterial.objects.filter(product__name=product_name)
            material_data = []

            for pm in product_materials:
                required_qty = pm.quantity * product_qty  # Kerakli umumiy miqdor
                warehouses = Warehouse.objects.filter(material=pm.material).order_by('id')

                for warehouse in warehouses:
                    # Agar material avval ishlatilgan bo'lsa, undan foydalanmaymiz
                    remaining_qty = warehouse.remainder - used_materials.get(warehouse.id, 0)

                    if required_qty <= 0 or remaining_qty <= 0:
                        continue

                    used_qty = min(remaining_qty, required_qty)
                    material_data.append({
                        "warehouse_id": warehouse.id,
                        "material_name": pm.material.name,
                        "qty": used_qty,
                        "price": int(warehouse.price)  # Faqat butun qiymat
                    })

                    # Band qilingan miqdorni saqlaymiz
                    used_materials[warehouse.id] = used_materials.get(warehouse.id, 0) + used_qty
                    required_qty -= used_qty

                # Agar yetarli xomashyo mavjud bo'lmasa
                if required_qty > 0:
                    material_data.append({
                        "warehouse_id": None,
                        "material_name": pm.material.name,
                        "qty": required_qty,
                        "price": None
                    })

            result.append({
                "product_name": product_name,
                "product_qty": product_qty,
                "product_materials": material_data
            })

        return Response({"result": result}, status=status.HTTP_200_OK)

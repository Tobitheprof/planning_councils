from itemadapter import ItemAdapter

class CouncilPipeline:
    FIELDS_TO_STRIP = {
        "reference": "reference",
        "application_validated": "application_validated",
        "application_received" : "application_received",
        "address": "address",
        "proposal": "proposal",
        "status": "status",
        "decision": "decision",
        "appeal_status": "appeal_status",
        "appeal_decision": "appeal_decision",
        "alt_ref": "alt_ref",
        "cases": "cases",
        "property": "property"
    }

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        for field, attribute in self.FIELDS_TO_STRIP.items():
            value = adapter.get(attribute)
            if value:
                adapter[attribute] = value.strip()

        return item


# class ChilternCouncilPipeline:
#     FIELDS_TO_STRIP = {
#         "reference" : "reference",
#         "application_validated" : "application_validated",
#         "address" : "address",
#         "proposal" : "proposal",
#         "status" : "status",
#         "appeal_status" : "appeal_status",
#         "appeal_decision" : "appeal_decision",
#         "documents" : "documents",
#         "cases": "cases",
#         "property": "property",

#     }

#     def process_item(self, item, spider):
#         adapter = ItemAdapter(item)

#         for field, attribute in self.FIELDS_TO_STRIP.items():
#             value = adapter.get(attribute)
#             if value:
#                 adapter[attribute] = value.strip()

#         return item

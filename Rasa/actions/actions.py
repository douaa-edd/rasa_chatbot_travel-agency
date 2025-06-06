from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


# ===============================
# Action: Recherche de vols
# ===============================
class ActionSearchFlights(Action):
    def name(self) -> Text:
        return "flight_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ville_depart = tracker.get_slot("ville_depart")
        ville_destination = tracker.get_slot("ville_destination")
        date_depart = tracker.get_slot("date_depart")
        classe = tracker.get_slot("classe")

        # Simuler une recherche (dans la vraie version, on interrogerait une API)
        dispatcher.utter_message(
            text=f"✅ تم العثور على رحلة من {ville_depart} إلى {ville_destination} بتاريخ {date_depart} في درجة {classe}."
        )

        return []


# ===============================
# Action: Recherche d'hôtels
# ===============================
class ActionSearchHotels(Action):
    def name(self) -> Text:
        return "hotel_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ville_hotel = tracker.get_slot("ville_hotel")
        categorie_hotel = tracker.get_slot("categorie_hotel")
        nombre_personnes = tracker.get_slot("nombre_personnes")

        dispatcher.utter_message(
            text=f"🏨 تم العثور على فندق {categorie_hotel} نجوم في {ville_hotel} لـ {nombre_personnes} أشخاص."
        )

        return []


# ===============================
# Action: Confirmation de réservation
# ===============================
class ActionConfirmReservation(Action):
    def name(self) -> Text:
        return "confirm_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="تم تأكيد الحجز بنجاح! ✅ شكراً لاستخدامك خدماتنا."
        )
        return []


# ===============================
# Action: Modifier une option
# ===============================
class ActionChangeOption(Action):
    def name(self) -> Text:
        return "edit_option"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="ما الخيار الذي تود تغييره؟ يمكنك مثلاً تغيير المدينة أو التاريخ."
        )
        return []


# ===============================
# Action: Sélection d'une option
# ===============================
class ActionSelectOption(Action):
    def name(self) -> Text:
        return "select_option"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        selected = tracker.get_slot("selected_option")
        dispatcher.utter_message(text=f"تم اختيار الخيار: {selected}")
        return [SlotSet("selected_option", selected)]



# ===============================
# Validation: flight_form
# ===============================
class ValidateFlightForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_flight"

    def validate_date_depart(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> Dict[Text, Any]:
        # Ici on pourrait ajouter une vérification de date réelle
        if slot_value:
            return {"date_depart": slot_value}
        else:
            dispatcher.utter_message(text="يرجى إدخال تاريخ صالح للسفر.")
            return {"date_depart": None}


# ===============================
# Validation: hotel_form
# ===============================
class ValidateHotelForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_hotel"

    def validate_nombre_personnes(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> Dict[Text, Any]:
        try:
            nombre = int(slot_value)
            if nombre > 0:
                return {"nombre_personnes": nombre}
            else:
                dispatcher.utter_message(text="يرجى إدخال عدد صحيح من الأشخاص.")
                return {"nombre_personnes": None}
        except ValueError:
            dispatcher.utter_message(text="يرجى إدخال رقم صحيح.")
            return {"nombre_personnes": None}

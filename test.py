import firebase as fb
import descriptions

fb.db.child("Description").update(descriptions.descriptions)
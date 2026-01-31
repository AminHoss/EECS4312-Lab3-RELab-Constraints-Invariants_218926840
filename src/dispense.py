
from datetime import date

class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.

    """

    # Assume the below is a dictionary including the max dosages for all medications in the form of 'medication_name':'maximum_dosage in mgs'
    MEDICATION_MAX_DOSAGE = {
        'vyvanse':75
    }

    # My reasoning for date being obtained on the dispense event instead of as an argument is that
    # In the real world, an actual dispensing machine would simply use its current date as the date
    # of the event as opposed to an argument from anywhere else
    # However for testing purposes I need to add an argument
    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    def __init__(self, patient_id, medication, dose_mg, quantity, date=date.today()):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.

        """
        self.patient_id = patient_id
        self.medication = medication.lower()

        self.date = date
        
        if not isinstance(dose_mg, (int,float)):
            raise TypeError("Dosage in milligrams must be a numerical value")
        elif dose_mg <=0:
            raise ValueError("Dosage must be a positive number")
        self.dose_mg = dose_mg
        
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        elif quantity <=0:
            raise ValueError("Quantity must be a positive integer")
        self.quantity = quantity

        if dose_mg * quantity > self.MEDICATION_MAX_DOSAGE[self.medication]:
            raise ValueError(f"Medication exceeds maximum dosage value of {self.MEDICATION_MAX_DOSAGE[self.medication]}")

        
            

    # TODO Task 4: Define and check system invariants 
    def invariant_holds(existing_events, new_event):
        """
        Check whether adding a new dispense event preserves all system invariants.

        Args:
            existing_events: Iterable of previously recorded DispenseEvent objects.
            new_event: The proposed DispenseEvent to validate.

        Returns:
            bool: True if all invariants hold after adding new_event; False otherwise.
            
        """
        if not isinstance(new_event, DispenseEvent):
            return False

        for event in existing_events:
            if event.patient_id == new_event.patient_id and event.medication == new_event.medication and event.date == new_event.date:
                return False

        return True
            

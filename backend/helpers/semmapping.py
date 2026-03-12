from helpers.semlinkedlist import SemLinkedList
from helpers.constants import SEASONS, TEST_CREDITS, TRANSFER_CREDITS, TRANSCRIPT_BEGINNING, TRANSCRIPT_END, STUDENT_ID

def get_sem_mapping(pdf_pages_list):

    sm_ll = SemLinkedList()
    parse_reg_undergrad = False
    
    for index, value in enumerate(pdf_pages_list):
        # Look for STUDENT ID 
        if STUDENT_ID in value and not parse_reg_undergrad:
            sm_ll.add((STUDENT_ID, index))
        elif value == TEST_CREDITS:
            sm_ll.add((TEST_CREDITS, index))
        elif value == TRANSFER_CREDITS:
            sm_ll.add((TRANSFER_CREDITS, index))
        
        elif value.startswith(TRANSCRIPT_BEGINNING):
            parse_reg_undergrad = True
        elif value.startswith(TRANSCRIPT_END):
            sm_ll.add((TRANSCRIPT_END, index))
        
        elif parse_reg_undergrad:
            for semester in SEASONS:
                if value.startswith(semester):
                    semester_info = value[len(semester):].strip()
                    semester_label = f"{semester} {semester_info}"
                    sm_ll.add((semester_label, index))
                    break
    return sm_ll
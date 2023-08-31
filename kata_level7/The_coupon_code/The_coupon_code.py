from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if len(str(entered_code)) != len(str(correct_code)):
        return False
    
    if entered_code == correct_code:
        cd = datetime.strptime(current_date, "%B %d, %Y")
        ed = datetime.strptime(expiration_date, "%B %d, %Y")
        
        if cd <= ed:
            return True
        else:
            return False
    
    else:
        return False

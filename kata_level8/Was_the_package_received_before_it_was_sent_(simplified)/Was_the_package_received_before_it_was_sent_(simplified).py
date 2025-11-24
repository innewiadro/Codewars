def was_package_received_yesterday(tz_from, tz_to, start, duration):
    utc_send = start - tz_from
    utc_arrival = utc_send + duration
    local_arrival = utc_arrival + tz_to
    return local_arrival < 0

    -- Run an SQL query on the messages database via shell script
    do shell script (["sqlite3 -line ~/Library/Messages/chat.db ", ¬
        "'SELECT MAX(date) lastMessageDate, h.id, text ", ¬
        "FROM message m INNER JOIN handle h ON h.ROWID=m.handle_id ", ¬
        "WHERE is_from_me = 0 GROUP BY h.ROWID' | egrep -io -e '\\w+ = .+'"] as text)
    
    set query_response to result
        --> lastMessageDate = %timestamp%
        --> id = %phone number or iMessage address%
        --> text = %message content%
        --> ...
    
    -- Groups all messages into a single item of an array
    -- Each occurence of  "lastMessageDate = " indicates 
    -- a new message and, hence, a new array item.
    set AppleScript's text item delimiters to "lastMessageDate = "
    set query_response to rest of text items of query_response
    
    -- Loop through the array organise each message
    repeat with message in query_response
        
        -- Split the array item up into its components
        set [receivedOn, sentFrom, textContent] ¬
            to [paragraph 1, ¬
            text 6 thru -1 of paragraph 2, ¬
            text 8 thru -1 of paragraph 3] of message
        
        -- Convert ReceivedOn to a value representing
        -- the number of days since 01/01/2001
        set receivedOn to receivedOn / (1.0E+9 * 86400)
        
        -- Convert ReceivedOn again to the date
        -- corresponding to the number of days since
        -- 01/01/2001, i.e. the date and time the message
        -- was sent
        set receivedOn to (date "Monday, 1 January 2001 at 00:00:00") + receivedOn * days
        
        --do something with the array
    end repeat
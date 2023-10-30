### Start (Задание 1)

```bash
docker-compose up --build -d
```



## Для выполнения процедуры (Задание 2)

SELECT update_short_names_status();

## Тело процедуры

CREATE FUNCTION update_short_names_status()

RETURNS VOID AS $$

DECLARE

    item TEXT;

BEGIN

    FOR item IN SELECT DISTINCT filename FROM full_names
    LOOP
        UPDATE full_names AS fn
        SET status = s.status
        FROM short_names AS s
        WHERE s.filename || item = fn.filename;
    END LOOP;

END;

$$ LANGUAGE plpgsql;


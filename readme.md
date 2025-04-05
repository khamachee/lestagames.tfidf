# Lesta games test task

### backend sample ```.env``` file 
```bash
DEBUGPY=0
REDIS_URL=redis://redis:6379/0
``` 

запуск бэка: ```docker compose up -d --build```  на папке ```backend```

запуск фронта ```docker compose up -d --build```  на папке ```frontend```

после этого:

веб приложение будет доступна по адресу : ```http://localhost:8080/```

бэк будет доступна по адресу: ```http://localhost:8000/```

(5678 порт расшарена тупо для дебаггинга через debugpy)


> по vue js у меня немножко плачебная ситуация. не особо умею использовать routing. 
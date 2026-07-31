<img width="822" height="318" alt="Screenshot 2026-07-27 at 9 33 23 PM" src="https://github.com/user-attachments/assets/fd19261a-a86b-4a96-a531-6e76cbe53939" />

<img width="866" height="353" alt="Screenshot 2026-07-27 at 9 35 32 PM" src="https://github.com/user-attachments/assets/1bb6e5ff-3df2-47ee-8d24-a5b531b4df36" />

```service-definition.yml```
```
apiVersion: v1
kind: Service
metadata:
    name: myapp-service

spec:
   type: NodePort
   ports:
     - targetPort: 80
       port: 80
       nodePort: 30008
   selector:
     app: myapp
     type: front-end

```

```
 kubectl create -f service-definition.yml

 kubectl get services

curl http://192.168.1.2:30008 
```
<img width="974" height="385" alt="Screenshot 2026-07-27 at 9 52 21 PM" src="https://github.com/user-attachments/assets/42016f36-4dd9-484e-b18f-d42f89955f85" />

<img width="896" height="428" alt="Screenshot 2026-07-27 at 10 27 24 PM" src="https://github.com/user-attachments/assets/ece3ef00-ebc1-4cf5-83e6-f1672e7f41a5" />

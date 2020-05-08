## NodeJS Setup

<details>
  <summary>Allow NodeJS to access ports</summary>
  
```sh
sudo setcap 'cap_net_bind_service=+ep' "path/to/bin"
```

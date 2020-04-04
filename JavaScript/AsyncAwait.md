## JavaScript async/await

<details>
  <summary>View Code</summary>
  
```js

async function getMessage(delay) {
  return new Promise((resolve, reject) => {
    let errors = false;
    
    if (errors) {
      reject("Something went wrong!");
      return false;
    }
  
    setTimeout(() => {
      resolve("Hello World!");  
    }, delay);
    
    return true;
  });
}

async function main() {
  const message = await getMessage(1000);
  console.log(message);
}

main();

```

# JavaScript Promises

## Promise using then and catch

<details>
  <summary>View Code</summary>
  
```js

const getMessage = (delay) => {
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

getMessage(1000).then(value => {
  console.log(value);
}).catch(ex => {
  console.log(ex)
});

```

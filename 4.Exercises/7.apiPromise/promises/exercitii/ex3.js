// 3. Build a function that returns a promise after 5 seconds. 
//    The promise must containing an array of numbers. 
//    Log the the numbers.

function getNumbers() {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve([1,2,3]), 5000);
  });
}


getNumbers() 
  .then((array) => console.log(array));


console.log('test4');
console.log('test5');
console.log('test6');


// functia trebuie sa returneze un promise dupa 5 secunde
// un promise care contine o lista de numere si pe care trebuie sa le trimitem la consola
// instantiem clasa promise, iar constructorul acelei clase primeste un callback
// callback care are doi parametrii, resolve si refect


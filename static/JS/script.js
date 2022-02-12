

let goal = document.getElementById('goal').innerHTML
// the only way "records" works is with the [] and then you only get the value at that index
// Taking away the .innerHTML gives you an array but of the element names, not value
// tried getElementsByClass, got same result
let records = document.querySelectorAll('.records')[0].innerHTML
let display = document.getElementById('display')

console.log(goal)
console.log(records)
display.innerText = eval(goal - records)


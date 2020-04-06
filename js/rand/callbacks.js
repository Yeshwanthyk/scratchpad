function doSomething(callback) {
   callback(1)
}

// doSomething(console.log)

function doSomethingAsync(callback) {
    setTimeout(function() {callback(1), 1000})
}

doSomethingAsync(console.log)

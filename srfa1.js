var log = function() {
    console.log.apply(console, arguments)
}

/*
判断一个素数
1. 素数 除 1 和 自身，没有其它约数，所以而 2 开始写除数
2. 确定 [2, x]，x = sqrt(n)，因为 2x8 等价于 8x2，所以算一半
*/

var prime = function(x) {
    for (var i = 2; i <= Math.sqrt(x); i++) {
        if (x % i == 0) {
            return false
        }
    }
    return true
}


var prime_array = function(n) {
    var plist = []
    for (var i = 2; i <= n; i++) {
        if (prime(i)) {
            plist.push(i)
        }
    }
    return log(plist)
}

prime_array(200)

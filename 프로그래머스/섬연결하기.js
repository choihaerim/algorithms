function solution(n, costs) {
    var answer = 0;
    costs.sort((a,b)=> a[2]-b[2])
    var cycleTable = Array(n).fill(0).map((element, index)=> index)
    
    while(!isOne(cycleTable)){
        var current = costs.shift()
        var one = current[0]
        var the_other = current[1]
        var cost = current[2]
        if(cycleTable[the_other] !== cycleTable[one]){
            cycleTable = changeCycleTableNumber(cycleTable, one, the_other)
            answer+=cost
        }
    }
    return answer;
}

function changeCycleTableNumber(cycleTable, one, the_other){
    var cycleTheOther = cycleTable[the_other]
    var cycleOne = cycleTable[one]
    for(var i=0; i<cycleTable.length; i++){
        if(cycleTable[i] === cycleTheOther) cycleTable[i] = cycleOne
    }
    return cycleTable 
}
    
function isOne(cycleTable){
    for(var i=1; i<cycleTable.length; i++){
        if(cycleTable[i-1] !== cycleTable[i]) return false 
    }
    return true 
}
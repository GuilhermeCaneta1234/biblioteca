var agora = new Date ()
horas = agora.getHours(8)
console.log (`agora sao exatamente ${horas} `)

if (horas<12){
console.log ("bom dia")
}
else if (horas<18) {
console.log("boa tarde")
}
else{
    console.log("Boa noite")
}

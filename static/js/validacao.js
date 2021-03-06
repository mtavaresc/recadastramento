/**
 * @return {string}
 */
function TestaCPF(elemento) {
    let cpf = elemento.value;
    cpf = cpf.replace(/[^\d]+/g, "");
    if (cpf === "")
        return elemento.style.borderColor = "red";
    // Elimina CPFs invalidos conhecidos    
    if (cpf.length !== 11 ||
        cpf === "00000000000" ||
        cpf === "11111111111" ||
        cpf === "22222222222" ||
        cpf === "33333333333" ||
        cpf === "44444444444" ||
        cpf === "55555555555" ||
        cpf === "66666666666" ||
        cpf === "77777777777" ||
        cpf === "88888888888" ||
        cpf === "99999999999")
        return elemento.style.borderColor = "red";
    // Valida 1o digito 
    let add = 0;
    for (let i = 0; i < 9; i++)
        add += parseInt(cpf.charAt(i)) * (10 - i);
    let rev = 11 - (add % 11);
    if (rev === 10 || rev === 11)
        rev = 0;
    if (rev !== parseInt(cpf.charAt(9)))
        return elemento.style.borderColor = "red";
    // Valida 2o digito 
    add = 0;
    for (let i = 0; i < 10; i++)
        add += parseInt(cpf.charAt(i)) * (11 - i);
    rev = 11 - (add % 11);
    if (rev === 10 || rev === 11)
        rev = 0;
    if (rev !== parseInt(cpf.charAt(10)))
        return elemento.style.borderColor = "red";
    return elemento.style.borderColor = "green";
}

//Required fields dynamic.
function requiredCtps() {
    const nrCTPS = document.getElementById("nrCTPS");
    const serieCtps = document.getElementById("serieCtps");
    const ufCtps = document.getElementById("ufCtps");

    if (!nrCTPS.required)
        jQuery(nrCTPS).attr('required', '');
    else
        jQuery(nrCTPS).removeAttr('required');

    if (!serieCtps.required)
        jQuery(serieCtps).attr('required', '');
    else
        jQuery(serieCtps).removeAttr('required');

    if (!ufCtps.required)
        jQuery(ufCtps).attr('required', '');
    else
        jQuery(ufCtps).removeAttr('required')
}

function requiredOC() {
    const nrOc = document.getElementById("nrOc");
    const orgaoEmissor = document.getElementById("oc_orgaoEmissor");
    const dtExped = document.getElementById("oc_dtExped");

    if (!nrOc.required)
        jQuery(nrOc).attr('pattern', '^[0-9]*$');
    else
        jQuery(nrOc).removeAttr('pattern');

    if (!orgaoEmissor.required)
        jQuery(orgaoEmissor).attr('pattern', '^[a-zA-Z\\s]*$');
    else
        jQuery(orgaoEmissor).removeAttr('pattern');

    if (!dtExped.required)
        jQuery(dtExped).attr('required', '');
    else
        jQuery(dtExped).removeAttr('required');
}

function requiredCNH() {
    const nrRegCnh = document.getElementById("nrRegCnh");
    const dtExped = document.getElementById("cnh_dtExped");
    const ufCnh = document.getElementById("ufCnh");
    const dtValid = document.getElementById("cnh_dtValid");
    const dtPriHab = document.getElementById("dtPriHab");
    const categoriaCnh = document.getElementById("categoriaCnh");

    if (!nrRegCnh.required)
        jQuery(nrRegCnh).attr('pattern', '^[0-9]*$');
    else
        jQuery(nrRegCnh).removeAttr('pattern');

    if (!dtExped.required)
        jQuery(dtExped).attr('required', '');
    else
        jQuery(dtExped).removeAttr('required');

    if (!ufCnh.required)
        jQuery(ufCnh).attr('required', '');
    else
        jQuery(ufCnh).removeAttr('required');

    if (!dtValid.required)
        jQuery(dtValid).attr('required', '');
    else
        jQuery(dtValid).removeAttr('required');

    if (!dtPriHab.required)
        jQuery(dtPriHab).attr('required', '');
    else
        jQuery(dtPriHab).removeAttr('required');

    if (!categoriaCnh.required)
        jQuery(categoriaCnh).attr('required', '');
    else
        jQuery(categoriaCnh).removeAttr('required');
}

function requiredDep() {
    const tpDep = document.getElementById("tpDep");
    const nmDep = document.getElementById("nmDep");
    const dtNascto = document.getElementById("dep_dtNascto");
    const cpfDep = document.getElementById("cpfDep");
    const depIRRF = document.getElementById("depIRRF");
    const depSF = document.getElementById("depSF");
    const incTrab = document.getElementById("incTrab");

    if (!tpDep.required)
        jQuery(tpDep).attr('required', '');
    else
        jQuery(tpDep).removeAttr('required');

    if (!nmDep.required)
        jQuery(nmDep).attr('pattern', '^[a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇ\\s]*$');
    else
        jQuery(nmDep).removeAttr('pattern');

    if (!dtNascto.required)
        jQuery(dtNascto).attr('required', '');
    else
        jQuery(dtNascto).removeAttr('required');

    if (!cpfDep.required)
        jQuery(cpfDep).attr('pattern', '^([0-9]{2}[\\.]?[0-9]{3}[\\.]?[0-9]{3}[\\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\\.]?[0-9]{3}[\\.]?[0-9]{3}[-]?[0-9]{2})$');
    else
        jQuery(cpfDep).removeAttr('pattern');

    if (!depIRRF.required)
        jQuery(depIRRF).attr('required', '');
    else
        jQuery(depIRRF).removeAttr('required');

    if (!depSF.required)
        jQuery(depSF).attr('required', '');
    else
        jQuery(depSF).removeAttr('required');

    if (!incTrab.required)
        jQuery(incTrab).attr('required', '');
    else
        jQuery(incTrab).removeAttr('required');
}

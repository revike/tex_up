function openWindow() {
    let modal = document.querySelector('.content_form')
    if (!modal.style['display']) {
        modal.style['display'] = 'flex'
    } else {
        modal.style['display'] = null
    }

    let phone = document.querySelector('#id_phone')
    phone.addEventListener('keyup', () => {
        if (phone.value.length === 1) {
            phone.value = '+7'
        }
    });
}

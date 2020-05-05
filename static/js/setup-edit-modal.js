/**
 * Contient les requetes permettant la modification et la suppression des utilisateur
 * 
 * @author: Tanguy Cavagna
 * @copyright: Copyright 2020, TPI
 * @version: 1.0.0
 * @date: 2020-05-05
 */

let edit_buttons = document.querySelectorAll('.edit');
let delete_buttons = document.querySelectorAll('.delete');
let update_button = document.querySelector('#update-user');

let edit_modal = document.querySelector('#edit-modal');
let first_name_edit = document.querySelector('#first-name-edit input');
let last_name_edit = document.querySelector('#last-name-edit input');
let email_edit = document.querySelector('#email-edit input');
let phone_edit = document.querySelector('#phone-edit input');

edit_buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        let idUser = btn.parentElement.dataset.userId;
        
        fetch('/get/user', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'idUser': idUser })
        })
        .then(response => {
            return response.json();
        })
        .then(json => {
            let user = json['User'];
            
            edit_modal.dataset.userId = user['id'];
            first_name_edit.value = user['first_name'];
            last_name_edit.value = user['last_name'];
            email_edit.value = user['email'];
            phone_edit.value = user['phone'];
        })
        .catch(err => {
            console.log(err);
        });
    });
});

delete_buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        let idUser = btn.parentElement.dataset.userId;
        
        fetch('/delete/user', {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'idUser': idUser })
        })
        .then(response => {
            return response.json();
        })
        .then(json => {
            window.location.reload();
        })
        .catch(err => {
            console.log(err);
        });
    });
});

update_button.addEventListener('click', () => {   
    fetch('/set/user', {
        method: 'PATCH',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            'idUser': edit_modal.dataset.userId,
            'lastnameUser': last_name_edit.value,
            'firstnameUser': first_name_edit.value,
            'emailUser': email_edit.value,
            'phoneUser': phone_edit.value,
        })
    })
    .then(response => {
        return response.json();
    })
    .then(json => {
        window.location.reload();
    })
    .catch(err => {
        console.log(err);
    });
});
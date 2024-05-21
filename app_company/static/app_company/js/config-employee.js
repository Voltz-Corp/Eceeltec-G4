const toasts = document.querySelectorAll('.toast');

function removeToast() {
    toasts.forEach(toast => {
        setTimeout(() => {
            toast.remove();
        }, 3000); 
    });
}

removeToast();
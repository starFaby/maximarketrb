from flask import request, render_template as render, flash
class ControllerAuth:
    def onGetControllerAuth():
        return render("auth/auth.html")
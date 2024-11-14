from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
        
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})

@views.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    if request.method == 'POST':
        data = request.form['note']
        note = Note.query.filter_by(id=id).first()
        note.data = data
        if len(note.data) < 1:
            flash('Note is too short!', category='error')
        else:    
            db.session.commit()
            flash('Note updated!', category='success')
            return redirect('/')

    note = Note.query.filter_by(id=id).first()
    return render_template('update.html', note=note , user=current_user)
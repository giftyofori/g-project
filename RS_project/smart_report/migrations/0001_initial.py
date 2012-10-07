# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table('student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_Name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_Name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('guardian_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('class_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('guardian_contact', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('smart_report', ['Student'])

        # Adding model 'Bill'
        db.create_table('bill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amnt_paid', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('amnt_due', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('balance', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=60)),
        ))
        db.send_create_signal('smart_report', ['Bill'])

        # Adding model 'School'
        db.create_table('school', (
            ('school_id', self.gf('django.db.models.fields.IntegerField')(max_length=20, primary_key=True)),
            ('school_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type_of_school', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('population', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('conctact', self.gf('django.db.models.fields.IntegerField')(max_length=14)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('smart_report', ['School'])

        # Adding model 'Teacher'
        db.create_table('teacher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('classes', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('course', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('smart_report', ['Teacher'])

        # Adding model 'Report'
        db.create_table('report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('class_score', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('exams_score', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('total_score', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('aggregate', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
        ))
        db.send_create_signal('smart_report', ['Report'])

        # Adding model 'Course'
        db.create_table('course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('num_of_subj', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('elective1', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('elective2', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('elective3', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('elective4', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('core1', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('core2', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('core3', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('core4', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('smart_report', ['Course'])

        # Adding model 'Hall'
        db.create_table('smart_report_hall', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('hall_teacher', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population', self.gf('django.db.models.fields.IntegerField')(max_length=124)),
        ))
        db.send_create_signal('smart_report', ['Hall'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table('student')

        # Deleting model 'Bill'
        db.delete_table('bill')

        # Deleting model 'School'
        db.delete_table('school')

        # Deleting model 'Teacher'
        db.delete_table('teacher')

        # Deleting model 'Report'
        db.delete_table('report')

        # Deleting model 'Course'
        db.delete_table('course')

        # Deleting model 'Hall'
        db.delete_table('smart_report_hall')


    models = {
        'smart_report.bill': {
            'Meta': {'object_name': 'Bill', 'db_table': "'bill'"},
            'amnt_due': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'amnt_paid': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'balance': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '60'})
        },
        'smart_report.course': {
            'Meta': {'object_name': 'Course', 'db_table': "'course'"},
            'core1': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'core2': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'core3': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'core4': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'elective1': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'elective2': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'elective3': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'elective4': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'num_of_subj': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        'smart_report.hall': {
            'Meta': {'object_name': 'Hall'},
            'hall_teacher': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'population': ('django.db.models.fields.IntegerField', [], {'max_length': '124'})
        },
        'smart_report.report': {
            'Meta': {'object_name': 'Report', 'db_table': "'report'"},
            'aggregate': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'class_score': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'exams_score': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_score': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'smart_report.school': {
            'Meta': {'object_name': 'School', 'db_table': "'school'"},
            'conctact': ('django.db.models.fields.IntegerField', [], {'max_length': '14'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'population': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'school_id': ('django.db.models.fields.IntegerField', [], {'max_length': '20', 'primary_key': 'True'}),
            'school_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type_of_school': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'smart_report.student': {
            'Meta': {'ordering': "['first_Name']", 'object_name': 'Student', 'db_table': "'student'"},
            'class_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'first_Name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'guardian_contact': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_Name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'smart_report.teacher': {
            'Meta': {'object_name': 'Teacher', 'db_table': "'teacher'"},
            'classes': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'course': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['smart_report']
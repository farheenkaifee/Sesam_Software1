# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/start_new_widget.ui'
#
# Created: Thu Sep 27 14:35:08 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_widget_start_new(object):
    def setupUi(self, widget_start_new):
        widget_start_new.setObjectName(_fromUtf8("widget_start_new"))
        widget_start_new.resize(995, 437)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_start_new.sizePolicy().hasHeightForWidth())
        widget_start_new.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtGui.QVBoxLayout(widget_start_new)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget_main_container = QtGui.QWidget(widget_start_new)
        self.widget_main_container.setObjectName(_fromUtf8("widget_main_container"))
        self.layout_main = QtGui.QVBoxLayout(self.widget_main_container)
        self.layout_main.setMargin(0)
        self.layout_main.setObjectName(_fromUtf8("layout_main"))
        spacerItem = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.layout_main.addItem(spacerItem)
        self.widget_central_container = QtGui.QWidget(self.widget_main_container)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_central_container.sizePolicy().hasHeightForWidth())
        self.widget_central_container.setSizePolicy(sizePolicy)
        self.widget_central_container.setObjectName(_fromUtf8("widget_central_container"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_central_container)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.widget_central_form = QtGui.QWidget(self.widget_central_container)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_central_form.sizePolicy().hasHeightForWidth())
        self.widget_central_form.setSizePolicy(sizePolicy)
        self.widget_central_form.setMinimumSize(QtCore.QSize(400, 0))
        self.widget_central_form.setObjectName(_fromUtf8("widget_central_form"))
        self.formLayout = QtGui.QFormLayout(self.widget_central_form)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setMargin(0)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.widget_header_start = QtGui.QWidget(self.widget_central_form)
        self.widget_header_start.setObjectName(_fromUtf8("widget_header_start"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_header_start)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setMargin(4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_get_started = QtGui.QLabel(self.widget_header_start)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_get_started.sizePolicy().hasHeightForWidth())
        self.label_get_started.setSizePolicy(sizePolicy)
        self.label_get_started.setObjectName(_fromUtf8("label_get_started"))
        self.horizontalLayout_2.addWidget(self.label_get_started)
        self.label_2 = QtGui.QLabel(self.widget_header_start)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.widget_header_start)
        spacerItem2 = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.formLayout.setItem(2, QtGui.QFormLayout.SpanningRole, spacerItem2)
        self.label_templates = QtGui.QLabel(self.widget_central_form)
        self.label_templates.setObjectName(_fromUtf8("label_templates"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_templates)
        self.list_templates = QtGui.QListWidget(self.widget_central_form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_templates.sizePolicy().hasHeightForWidth())
        self.list_templates.setSizePolicy(sizePolicy)
        self.list_templates.setMaximumSize(QtCore.QSize(16777215, 50))
        self.list_templates.setObjectName(_fromUtf8("list_templates"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.list_templates)
        self._label_recent = QtGui.QLabel(self.widget_central_form)
        self._label_recent.setObjectName(_fromUtf8("_label_recent"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self._label_recent)
        self.list_recent = QtGui.QListWidget(self.widget_central_form)
        self.list_recent.setMaximumSize(QtCore.QSize(16777215, 100))
        self.list_recent.setObjectName(_fromUtf8("list_recent"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.list_recent)
        self.label_browse = QtGui.QLabel(self.widget_central_form)
        self.label_browse.setObjectName(_fromUtf8("label_browse"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_browse)
        self.button_browse = QtGui.QCommandLinkButton(self.widget_central_form)
        self.button_browse.setObjectName(_fromUtf8("button_browse"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.button_browse)
        self.label_help = QtGui.QLabel(self.widget_central_form)
        self.label_help.setObjectName(_fromUtf8("label_help"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_help)
        self.widget_3 = QtGui.QWidget(self.widget_central_form)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.button_osdoc = QtGui.QCommandLinkButton(self.widget_3)
        self.button_osdoc.setObjectName(_fromUtf8("button_osdoc"))
        self.horizontalLayout_3.addWidget(self.button_osdoc)
        self.button_forum = QtGui.QCommandLinkButton(self.widget_3)
        self.button_forum.setObjectName(_fromUtf8("button_forum"))
        self.horizontalLayout_3.addWidget(self.button_forum)
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.widget_3)
        self.widget_header_new = QtGui.QWidget(self.widget_central_form)
        self.widget_header_new.setObjectName(_fromUtf8("widget_header_new"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_header_new)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setMargin(4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_start_new = QtGui.QLabel(self.widget_header_new)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_start_new.sizePolicy().hasHeightForWidth())
        self.label_start_new.setSizePolicy(sizePolicy)
        self.label_start_new.setObjectName(_fromUtf8("label_start_new"))
        self.horizontalLayout_4.addWidget(self.label_start_new)
        self.label = QtGui.QLabel(self.widget_header_new)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.button_cancel = QtGui.QPushButton(self.widget_header_new)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cancel.sizePolicy().hasHeightForWidth())
        self.button_cancel.setSizePolicy(sizePolicy)
        self.button_cancel.setObjectName(_fromUtf8("button_cancel"))
        self.horizontalLayout_4.addWidget(self.button_cancel)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.widget_header_new)
        self.horizontalLayout.addWidget(self.widget_central_form)
        spacerItem3 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.layout_main.addWidget(self.widget_central_container)
        spacerItem4 = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.layout_main.addItem(spacerItem4)
        self.widget_credits = credits_widget(self.widget_main_container)
        self.widget_credits.setObjectName(_fromUtf8("widget_credits"))
        self.layout_main.addWidget(self.widget_credits)
        self.verticalLayout_2.addWidget(self.widget_main_container)

        self.retranslateUi(widget_start_new)
        QtCore.QMetaObject.connectSlotsByName(widget_start_new)

    def retranslateUi(self, widget_start_new):
        widget_start_new.setWindowTitle(QtGui.QApplication.translate("widget_start_new", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_get_started.setText(QtGui.QApplication.translate("widget_start_new", "ICON", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("widget_start_new", "<b>Get started!</b><br />\n"
"<small><i>Select an item in the overview area to start right away</i></small>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_templates.setText(QtGui.QApplication.translate("widget_start_new", "<h3>New</h3>", None, QtGui.QApplication.UnicodeUTF8))
        self._label_recent.setText(QtGui.QApplication.translate("widget_start_new", "<h3>Recent</h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_browse.setText(QtGui.QApplication.translate("widget_start_new", "<h3>Open</h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.button_browse.setText(QtGui.QApplication.translate("widget_start_new", "Open an existing experiment", None, QtGui.QApplication.UnicodeUTF8))
        self.label_help.setText(QtGui.QApplication.translate("widget_start_new", "<h3>Help</h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.button_osdoc.setText(QtGui.QApplication.translate("widget_start_new", "Visit the documentation site", None, QtGui.QApplication.UnicodeUTF8))
        self.button_forum.setText(QtGui.QApplication.translate("widget_start_new", "Ask a question on the forum", None, QtGui.QApplication.UnicodeUTF8))
        self.label_start_new.setText(QtGui.QApplication.translate("widget_start_new", "ICON", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("widget_start_new", "<b>New expriment</b><br />\n"
"<small><i>Click \'cancel\' or close this tab to another tab to resume your current experiment</i></small>", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel.setText(QtGui.QApplication.translate("widget_start_new", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

from libqtopensesame.widgets.credits_widget import credits_widget

.. image:: https://travis-ci.org/lrowe/pyramid_localroles.svg?branch=master
    :target: https://travis-ci.org/lrowe/pyramid_localroles

Local roles authorization policy for Pyramid
============================================

Objects may be given an ``__ac_local_roles__`` property which may be either a
mapping or a callable that returns a mapping from principal id to a list of principals.

Heritage
--------

This package is modelled closesly on the local role system in Zope/CMF/Plone.

Plone allowedRolesAndUsers
  https://github.com/plone/Products.CMFPlone/blob/master/Products/CMFPlone/CatalogTool.py

Plone _getAllLocalRole
  https://github.com/plone/Products.PlonePAS/blob/master/Products/PlonePAS/pas.py

CMF allowedRolesAndUsers
  http://svn.zope.org/Products.CMFCore/trunk/Products/CMFCore/CatalogTool.py

CMF _mergedLocalRoles
  http://svn.zope.org/Products.CMFCore/trunk/Products/CMFCore/utils.py

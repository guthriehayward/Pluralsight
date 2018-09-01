#!/usr/bin/env python3
"""
Experimentation with set algebra.

Usage: Just practicing

    python3 setFun.py
"""
#People with blue eyes
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}

#People with blond hair
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}

#People who can smell hydrogen cyanide
smell_hcn = {'Harry', 'Amelia'}

#People who can taste phenylthiocarbamide
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}

#BLood types
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia}'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

#Find people with either blue eyes or blond blond hair
blue_eyes.union(blond_hair)

#Find people with blue eyes and blond hair
blue_eyes.intersection(blond_hair)

#note that union and intersection are commmutative:
blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes)
blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes)

#Find people with blond hair who do not have blue eyes
blond_hair.difference(blue_eyes)

#note that difference is NOT commmutative
blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair)

#people who have either blond hair OR blue eyes, but NOT both
blond_hair.symmetric_difference(blue_eyes)

#note that symmetric_difference IS commmutative
blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair)

#Do all people who can smell hydrogen cyanide have blond hair?
smell_hcn.issubset(blond_hair)

#Can all people who can taste phenylthiocarbamide also smell hydrogen cyanide?
taste_ptc.issuperset(smell_hcn)

#Do two groups have no common members? I.e. blood types
a_blood.isdisjoint(o_blood)

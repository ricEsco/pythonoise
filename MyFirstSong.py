#!/usr/bin/env python3

from midiutil import MIDIFile

# Defining variables -----------------------------------------------------------------------------
ch2      = [68, 71, 68, 71, 69, 71, 69, 71, 69, 71, 69, 71, 68, 71, 68, 71, 68, 76, 71, 76, 75, 81, 71, 75, 71, 76, 68, 71, 69, 71, 69, 71, 69, 71, 69, 71, 68, 71, 68, 71, 68]
ch1      = [73, 75, 73, 75, 73, 75, 73, 75]
ch0A     = [80, 80, 78]
ch0B     = [81, 81, 80]
ch0C     = [83, 81, 80, 75, 76]
ch0D     = [80, 80, 78]
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
qnote    = 1    # quarter note
enote    = 0.5  # eigth note
snote    = 0.25 # sixteenth note
tempo    = 36   # Integer in BPM
volume   = 100

# MIDIFile() creates the midi file ---------------------------------------------------------------
# removeDuplicates -> If set to True (the default), duplicate notes will be removed from the file.
mf = MIDIFile(1, removeDuplicates=False)
# MIDIFileArgs:(numTracks=1, removeDuplicates=True, deinterleave=True, adjust_origin=False, file_format=1, ticks_per_quarternote=960, eventtime_is_ticks=False)

# Adds the tempo to the file
mf.addTempo(track, time, tempo)
# TempoArgs:(track, time, tempo)

# ProgramChange -> Change the voice (instrument) of the pitch
# Have to do it for each channel being used and they can be different
mf.addProgramChange(track, 0, time, 0)
mf.addProgramChange(track, 1, time, 0)
mf.addProgramChange(track, 2, time, 0)
# ProgramChangeArgs:(track, channel, time, program)

# ControllerChange -> Controls various dynamics of pitch .i.e. mod wheel(1), pan(10), and sustain(64)
mf.addControllerEvent(track, 0, time, 10, 0)
mf.addControllerEvent(track, 1, time, 10, 0)
mf.addControllerEvent(track, 2, time, 10, 127)
# ControllerEventArgs(track, channel, time, controller_number, parameter)

# Start adding music notes -----------------------------------------------------
time = 0
# Beginning note is a dotted quarter note
mf.addNote(track,       0,    71, time + 0.5,    enote, volume)
# NoteArgs:(track,channel, pitch,       time, duration, volume, annotation=None)

# Begin the following notes after the dotted quarter note
time = 1
# Channel 2 notes are lowest notes
for i, pitch in enumerate(ch2):
    mf.addNote(track, 2, pitch, time, snote, volume)
    time += snote

# Restart time to overlay notes of different channels
time = 1
# Channel 1 notes are middle notes
mf.addNote(track, 1, 75, 2  , qnote, volume)
mf.addNote(track, 1, 75, 3.5, snote, volume)
mf.addNote(track, 1, 76, 4  , snote, volume)
time = 8
for i, pitch in enumerate(ch1):
    mf.addNote(track, 1, pitch, time, snote, volume)
    time += snote

# Restart time to overlay notes of different channels
time = 1
# Channel 0 notes are highest notes
mf.addNote(track, 0, 76, time, qnote, volume)
mf.addNote(track, 0, 75, 1.5 , snote, volume)
mf.addNote(track, 0, 76, 1.75, snote, volume)
mf.addNote(track, 0, 78, 2   , qnote, volume)
time = 3.25
for i, pitch in enumerate(ch0A):
    mf.addNote(track, 0, pitch, time, snote, volume)
    time += snote
mf.addNote(track, 0, 80, 4   , qnote, volume)
time = 5.25
for i, pitch in enumerate(ch0B):
    mf.addNote(track, 0, pitch, time, snote, volume)
    time += snote
mf.addNote(track, 0, 85, 6   , 0.75 , volume)
time = 6.75
for i, pitch in enumerate(ch0C):
    mf.addNote(track, 0, pitch, time, qnote, volume)
    time += snote
mf.addNote(track, 0, 78, 8   , qnote, volume)
time = 9.25
for i, pitch in enumerate(ch0D):
    mf.addNote(track, 0, pitch, time, snote, volume)
    time += snote
mf.addNote(track, 0, 76, 10 , qnote, volume)

# Finally, write the file to a file object -----------
with open("tristesseV4.mid", "wb") as output_file:
    mf.writeFile(output_file)
#Args:          (fileHandle)

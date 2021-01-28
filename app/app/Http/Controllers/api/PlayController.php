<?php

namespace App\Http\Controllers\api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Play;
use App\Http\Resources\PlayResource;

class PlayController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $plays = Play::paginate(25);
        return PlayResource::collection($plays);
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $title = $request->input('title')->all();
        $path = $request->input('path')->all();

        $play = new Play();
        $play->title = $title;
        $play->path = $path;
        
        $play->save();

        return response()->json([
            'message' => 'Play Created!'
        ],200);
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        $play = Play::findOrFail($id);
        return new PlayResource($play);
    }



    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        $play = Play::findOrFail($id);
        $play->title = $request->title;
        $play->path = $request->path;
        if($play->save())
        {
            new PlayResource($play);
        }
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        $play = Play::findOrFail($id);
        if($play->delete())
        {
            return new PlayResource($play);
        }
    }
}
